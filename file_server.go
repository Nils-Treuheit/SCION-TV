/*
Serve is a very simple static file server in go
Usage:
        -p="8899": port to serve on
        -d="path/to/html/hls":    the directory of static files to host
Navigating to http://localhost:8899 will display the index.html or directory
listing file.
*/
package main

import (
        "flag"
        "log"
        "net/http"
)

func main() {
        port := flag.String("p", "8899", "port to serve on")
        directory := flag.String("d", "./hls", "the directory of static file to host")
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