/*
Serve is a very simple static file server in go
Usage:
        -p="8899": port to serve on
        -d="path/to/hls":    the directory of static files to host
Navigating to http://localhost:8899 will display the directory file listings.
*/
package main

import (
        "flag"
        "log"
        "net/http"
        "os"
)

func main() {
        dir := "./hls"
        args := os.Args[1:]
        if len(args)>0 { os.Chdir(args[0]) } else {
         fmt.Println("Warning! You did not provide the absolute path to the loacation of your hls folder.")
         log.Println("Default to relative path...") }
        path, err := os.Getwd()
        if err != nil { log.Println(err) } else { dir = path+"/hls" }
        
        port := flag.String("p", "8899", "port to serve on")
        directory := flag.String("d", dir, "the directory of static file to host")
        flag.Parse()

        http.Handle("/", addHeaders(http.FileServer(http.Dir(*directory))))

        log.Printf("Serving %s on HTTP port: %s\n", *directory, *port)
        log.Fatal(http.ListenAndServe(":"+*port, nil))
}

// addHeaders will act as middleware to give us CORS support
func addHeaders(h http.Handler) http.HandlerFunc {
        return func(w http.ResponseWriter, r *http.Request) {
                w.Header().Set("Access-Control-Allow-Origin", "*")
                h.ServeHTTP(w, r)
        }
}
