kelvin
======
A simple internet of things application. It consists of a client application which reads the current temperature and pressure from a BMP085 sensor. It then sends this information to a web service via a hardware agnostic REST interface. The REST interface also makes the information available to read, which is used to display a graph of the last 24 hours of measurements.