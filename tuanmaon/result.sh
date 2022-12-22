#!/bin/bash
# Testing different methods for grabbing all the parameters
#
echo
echo "Using the \$@ method: $@"
str=$1
cd image_source/


if [ -f $str ]
then
	echo "$str资源文件存在,工作正在进行中"
	cd ..
	shift	
	for param in "$@"
	do
		echo "$param功能正在运行中"
		case $param in 
		1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10)
			cd image_source/
			cp $str ../answers1_py/$str
			cd ..
			cd answers1_py/
			#pwd
			run_file_name="answer_$param.py"
			python3 -W ignore $run_file_name
			mv $str ../gc/
			cd ..
			#pwd
			echo "$run_file_name成功";; 
		11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20)
			cd image_source/
			cp $str ../answers2_py/$str
			cd ..
			cd answers2_py/
			#pwd
			run_file_name="answer_$param.py"
			python3 -W ignore $run_file_name
			mv $str ../gc/
			cd ..
			#pwd
			echo "$run_file_name成功";;
		21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30)
			cd image_source/
			cp $str ../answers3_py/$str
			cd ..
			cd answers3_py/
			#pwd
			run_file_name="answer_$param.py"
			python3 -W ignore $run_file_name
			mv $str ../gc/
			cd ..
			#pwd
			echo "$run_file_name成功";;
		31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40)
			cd image_source/
			cp $str ../answers4_py/$str
			cd ..
			cd answers4_py/
			#pwd
			run_file_name="answer_$param.py"
			python3 -W ignore $run_file_name
			mv $str ../gc/
			cd ..
			#pwd
			echo "$run_file_name成功";;
		41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50)
			cd image_source/
			cp $str ../answers5_py/$str
			cd ..
			cd answers5_py/
			#pwd
			run_file_name="answer_$param.py"
			python3 -W ignore $run_file_name
			mv $str ../gc/
			cd ..
			#pwd
			echo "$run_file_name成功";;
		esac
	done
else
	echo "该资源文件不存在"
	exit
fi

exit
