WD=/home/shlomi/opencv-4.1.0/samples/python

cd:
	@cd $(WD)

1: cd
	python $(WD)/texture_flow.py
2: cd
	@cd $(WD)
	@python squares.py
