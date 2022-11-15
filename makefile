APKLIST = $(foreach n,$(shell echo *.apk),$(basename $(n)))
NEWAPKLIST = $(addprefix output/,$(shell echo *.apk))
## change it to your own
PYTHON = /c/Users/HP/AppData/Local/Programs/Python/Python39/python

ALL: depackage modify package sign run

depackage:
	@echo Detected `echo *.apk | wc -w` apk\(s\).
	@for i in `echo *.apk`; do echo depackaging $$i... && apktool d $$i;done
 
test:
	@echo $(APKLIST)
	@echo $(NEWAPKLIST)

package:
	@if ! [ -e output ]; then mkdir -p output; fi;
	@echo Leave apks in $(abspath output)
	@for i in $(APKLIST);do echo packaging $$i.apk && apktool b $$i -o output/$$i.apk;done

sign:
	@for i in $(APKLIST);do echo 123456 | jarsigner -verbose -signedjar output/$$i.apk output/$$i.apk apks;done

run:
	@if ! [ -e result ]; then mkdir -p result; fi;
	@for i in $(APKLIST);do java -jar fsquadra/FSquaDRA-master.jar $$i.apk output/$$i.apk -o result/result-$$i.csv;done
	@find . | grep result- | xargs $(PYTHON) csvmerger.py

modify:
	@for i in $(APKLIST);do find $$i/res/ | grep --regex ".*\.png" | xargs $(PYTHON) dissimulator.py;done

clean:
	-@for i in $(APKLIST);do rm -r $$i;done
#	@if [ -e output ]; then rm -r output; fi;

clean-all: clean
	-@if [ -e output ]; then rm -r output; fi;
	-@if [ -e result ]; then rm -r result; fi;
	-rm *.csv