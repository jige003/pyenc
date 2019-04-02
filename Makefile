TARGET=/usr/local/bin/pyenc

install:
	cp -f  pyenc.py $(TARGET)
	chmod +x $(TARGET)

uninstall:
	rm -f $(TARGET)
