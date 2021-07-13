/*
Serve is a very simple static file server in go
Usage:
        -p="80": port to serve on
        -f="/path/website/index.html": website to serve
Navigating to http://localhost:80 will display the index.html.
*/
package main

import (
        "flag"
        "log"
        "net/http"
        "os"
        "fmt"
)

func main() {
        website := "./index.html"
        icon := "./favicon.ico"
        pic := "./background.png"
        args := os.Args[1:]
        if len(args)>0 { os.Chdir(args[0]) } else {
         fmt.Println("Warning! You did not provide the absolute path to the loacation of the Website.")
         log.Println("Default to relative path...")
        }
        path, err := os.Getwd()
        if err != nil { log.Println(err) } else {
         website = path+"/index.html"
         icon = path+"/favicon.ico"
         pic = path+"/background.png"
        }

        port := flag.String("p", "80", "port to serve on")
        websiteHandle := flag.String("f", website, "the directory of static file to host")
        flag.Parse()

        http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request){http.ServeFile(w, r, website)})
        http.HandleFunc("/favicon.ico", func(w http.ResponseWriter, r *http.Request){http.ServeFile(w, r, icon)})
        http.HandleFunc("/background.png", func(w http.ResponseWriter, r *http.Request){http.ServeFile(w, r, pic)})
  
        log.Printf("Serving %s on HTTP port: %s\n", *websiteHandle, *port)
        log.Fatal(http.ListenAndServe(":"+*port, nil))
}
  
