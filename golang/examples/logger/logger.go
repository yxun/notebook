package logger

import (
	"github.com/sirupsen/logrus"
)

// Event logging id and message
type Event struct {
	id      int
	message string
}

// StandardLogger default logger
type StandardLogger struct {
	*logrus.Logger
}

// NewTextLogger default logger format in text
func NewTextLogger() *StandardLogger {
	var baseLogger = logrus.New()
	var standardLogger = &StandardLogger{baseLogger}
	standardLogger.Formatter = &logrus.TextFormatter{
		FullTimestamp: true,
	}
	return standardLogger
}

// NewJSONLogger logger format in JSON
func NewJSONLogger() *StandardLogger {
	var baseLogger = logrus.New()
	var standardLogger = &StandardLogger{baseLogger}
	standardLogger.Formatter = &logrus.JSONFormatter{}
	return standardLogger
}
