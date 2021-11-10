package main 

/*
This program starts a Webpage-Server, a File-Server with a header to support hosting of streaming content and a SCION-IP proxy
Usage:
        -webServPort="8080": port to serve webpage on [default = 8080]
        -webDir="/path/to/website-dir": website directory that contains index.html file and other elements to host [on port 8080]
        -fileServPort="8899": port to serve streaming files on [default = 8899]
        -fileDir="path/to/hls-folder": the directory of streaming files to host [on port 8899]
		-local="0.0.0.0:8890": specify IP-address and port the proxy should listen to
		-remote="19-ffaa:1:bcc,[127.0.0.1]:9001": specify SCION-address and port the proxy should remote to
*/
import (
	"fmt"
	"log"
	"flag"
	"net/http"
	"crypto/tls"
	"net/http/httputil"
	"net/url"

	"github.com/netsec-ethz/scion-apps/pkg/shttp"
	"github.com/scionproto/scion/go/lib/snet"
)

func main() {

	local := flag.String("local", "0.0.0.0:8890", "The local HTTP or SCION address on which the server will be listening")
	remote := flag.String("remote", "19-ffaa:1:bcc,[127.0.0.1]:9001", "The SCION or HTTP address on which the server will be requested")
	webServPort := flag.String("webServPort", "8080", "The port to serve website on")
	webDir := flag.String("webDir", "html", "The directory of static webpage elements to host")
	fileServPort := flag.String("fileServPort", "8899", "The port to serve website on")
	fileDir := flag.String("fileDir", "hls", "The directory of streaming content to host")
	flag.Parse()

	go file_server(fileDir,fileServPort)
	go web_server(webDir,webServPort)
	proxy(local,remote)

}

/*
PLEASE NOTE:
------------
This proxy implementation is pretty much a copy of the proxy implementation from the official scion-apps repository[https://github.com/netsec-ethz/scion-apps]
The current implementation of the official proxy can be found here[https://github.com/netsec-ethz/scion-apps/blob/master/_examples/shttp/proxy/main.go].
There will be differences between mine and the linked implementation since the repositories are not synced.

This proxy is used as a SCION to IP bridge in order to make a broadcasted MuMuDVB-Stream available to the local machine/network.
The proxy will be used as a SCION ingress proxy.

Navigating to http://localhost:8890 to access the MuMuDVB-Stream.
*/
func proxy(local *string, remote *string) {

	mux := http.NewServeMux()

	// parseUDPAddr validates if the address is a SCION address
	// which we can use to proxy to SCION
	if _, err := snet.ParseUDPAddr(*remote); err == nil {
		proxyHandler, err := shttp.NewSingleSCIONHostReverseProxy(*remote, &tls.Config{InsecureSkipVerify: true, NextProtos: []string{"h3"}})
		if err != nil {
			log.Fatalf("Failed to create SCION reverse proxy %s", err)
		}

		mux.Handle("/", proxyHandler)
		log.Printf("Proxy connected to SCION remote %s\n", *remote)
	} else {
		u, err := url.Parse(*remote)
		if err != nil {
			log.Fatal(fmt.Sprintf("Failed parse remote %s, %s", *remote, err))
		}
		log.Printf("Proxy connected to HTTP remote %s\n", *remote)
		mux.Handle("/", httputil.NewSingleHostReverseProxy(u))
	}

	if lAddr, err := snet.ParseUDPAddr(*local); err == nil {
		log.Printf("Proxy listens on SCION %s\n", *local)
		// ListenAndServe does not support listening on a complete SCION Address,
		// Consequently, we only use the port (as seen in the server example)
		log.Fatalf("%s", shttp.ListenAndServe(fmt.Sprintf(":%d", lAddr.Host.Port), mux, nil))
	} else {
		log.Printf("Proxy listens on HTTP %s\n", *local)
		log.Fatalf("%s", http.ListenAndServe(*local, mux))
	}
}


/*
This is a very simple webpage server in go
Navigating to http://localhost:8080 will display the index.html.
*/
func web_server(webDir *string, port *string) {
	webpage := "index.html"
	website := *webDir+"/"+webpage
	icon := *webDir+"/favicon.ico"
	pic := *webDir+"/background.png"

	mux := http.NewServeMux()
	mux.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){http.ServeFile(w, r, website)})
	mux.HandleFunc("/favicon.ico", func(w http.ResponseWriter, r *http.Request){http.ServeFile(w, r, icon)})
	mux.HandleFunc("/background.png", func(w http.ResponseWriter, r *http.Request){http.ServeFile(w, r, pic)})

	log.Printf("Web-Server serves %s webpage and its elements on HTTP port: %s\n", webpage, *port)
	log.Fatalf("%s", http.ListenAndServe(":"+*port, mux))
}


/*
This is a very simple static file server in go
Navigating to http://localhost:8899 will display the directory file listings.
*/
func file_server(directory *string, port *string) {

	mux := http.NewServeMux()
	mux.Handle("/", addHeaders(http.FileServer(http.Dir(*directory))))

	log.Printf("File-Server serves %s folder's streaming content on HTTP port: %s\n", *directory, *port )
	log.Fatalf("%s", http.ListenAndServe(":"+*port, mux))
}

// addHeaders will act as middleware to give us CORS support
func addHeaders(h http.Handler) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
			w.Header().Set("Access-Control-Allow-Origin", "*")
			h.ServeHTTP(w, r)
	}
}