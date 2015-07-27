PROJECT=petname

clean:
	rm -rf MANIFEST dist/* $(PROJECT).egg-info .coverage
	find . -name '*.pyc' -delete
