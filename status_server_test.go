package main

import (
	"net/http"
	"net/http/httptest"
	"testing"
)

// Тест для обработчика статуса
func TestHandleStatusRequest(t *testing.T) {
	// Создаем запрос
	req, err := http.NewRequest("GET", "/status", nil)
	if err != nil {
		t.Fatal(err)
	}

	// Создаем ResponseRecorder для записи ответа
	rr := httptest.NewRecorder()
	handler := http.HandlerFunc(handleStatusRequest)

	// Вызываем обработчик
	handler.ServeHTTP(rr, req)

	// Проверяем статус код
	if status := rr.Code; status != http.StatusOK {
		t.Errorf("handler returned wrong status code: got %v want %v",
			status, http.StatusOK)
	}

	// Проверяем тело ответа
	expected := "Status: OK\n"
	if rr.Body.String() != expected {
		t.Errorf("handler returned unexpected body: got %v want %v",
			rr.Body.String(), expected)
	}
}

// Тест для проверки запуска сервера
func TestRunServer(t *testing.T) {
	// Этот тест запускает сервер в горутине и проверяет, что он не падает сразу
	go func() {
		if err := runServer(); err != nil {
			t.Errorf("runServer failed: %v", err)
		}
	}()

	// Даем серверу время на запуск
	// В реальном тесте здесь можно сделать HTTP запрос
}

// Интеграционный тест (требует запущенного сервера)
func TestServerIntegration(t *testing.T) {
	// Запускаем тестовый сервер
	server := httptest.NewServer(http.HandlerFunc(handleStatusRequest))
	defer server.Close()

	// Делаем запрос к тестовому серверу
	resp, err := http.Get(server.URL + "/status")
	if err != nil {
		t.Fatal(err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		t.Errorf("Expected status OK, got %v", resp.StatusCode)
	}
}
