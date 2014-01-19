#!/bin/bash
echo "$1"
Path="/home/sem/chayadocs/"


isfile()
{
	i=$1
	echo "th file is :$i"
    CHARSET="$(file -bi "$i"|awk -F "=" '{print $2}')"
    	echo "$CHARSET"
		if [ "$CHARSET" != utf-8 ]; then
			mv $i $i.old
	        iconv -f "$CHARSET" -t utf8 "$i.old" -o "$i"
	        echo "convet $i\n"
	    else
	    	echo "$i is alredy utf8 file"
		fi
}

isdir()
{
	echo " this is a dir: $1 , $2"
	Pathn="$1"
	run $Pathn

}

run()
{
	echo "from run arg is:$1\n"

	for i in $( ls $1 ); do
		echo "$i"
		Dir=$1"/"$i
		echo "dir is $Dir"
		if [ -f "$Dir" ]; then
			isfile "$1/$i"
		else
			isdir "$1/$i"
		fi
		if [ -d "$1/$i" ]; then
			echo "$1"
			isdir "$1/$i"
		fi
	done
}
run "$Path"

# for i in $( ls $1 ); do
# 	echo "$i . $0"
# 	if [ -f $1$i ]; then
#     CHARSET="$(file -bi "$i"|awk -F "=" '{print $2}')"

# 		if [ "$CHARSET" != utf-8 ]; then
# 			mv $i $i.old
# 	        iconv -f "$CHARSET" -t utf8 "$i.old" -o "$i"
# 	        echo "convet $i\n"
# 	    else
# 	    	echo "$i is alredy utf8 file"
# 		fi
#     fi   
#     if [ -d $1$i ]; then
#     	echo "run on new dir $0 $1$i"
#     	`$0 $1$i`

#     fi

# done