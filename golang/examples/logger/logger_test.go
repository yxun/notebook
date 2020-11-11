package logger

import (
	"testing"
)

var log = NewTextLogger()

func TestLogger(t *testing.T) {
	t.Run("TextLogger", func(t *testing.T) {
		log.Infof("This is a test log: %s", "info")
		log.Errorf("This is an error log: %s", "Error log")
	})
}
