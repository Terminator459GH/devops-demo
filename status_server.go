package main

import (
	"fmt"
	"net/http"
)

func handleStatusRequest(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintln(w, "Status: OK")
}

func runServer() error {
	http.HandleFunc("/status", handleStatusRequest)
	fmt.Println("Starting server on :8080")
	return http.ListenAndServe(":8080", nil)
}

func main() {
	if err := runServer(); err != nil {
		fmt.Printf("Server error: %v\n", err)
	}
}
