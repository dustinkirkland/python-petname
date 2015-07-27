PROJECT=petname

clean:
	rm -rf MANIFEST dist/* $(PROJECT).egg-info .coverage build/*
	find . -name '*.pyc' -delete
