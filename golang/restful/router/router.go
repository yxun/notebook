package router

import (
	"github.com/yxun/go-examples/restful/controllers"

	"github.com/gorilla/mux"
)

// Router is exported and used in main.go
func Router() *mux.Router {

	router := mux.NewRouter()

	router.HandleFunc("/api/user/{id}", controllers.GetUser).Methods("GET", "OPTIONS")
	router.HandleFunc("/api/user", controllers.GetAllUser).Methods("GET", "OPTIONS")
	router.HandleFunc("/api/newuser", controllers.CreateUser).Methods("POST", "OPTIONS")
	router.HandleFunc("/api/user/{id}", controllers.UpdateUser).Methods("PUT", "OPTIONS")
	router.HandleFunc("/api/deleteuser/{id}", controllers.DeleteUser).Methods("DELETE", "OPTIONS")
	return router
}
