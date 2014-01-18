#!/bin/sh
echo "$1"
for i in $( ls $1 ); do
	echo "$i . $0"
	if [ -f $i ]; then
    CHARSET="$(file -bi "$i"|awk -F "=" '{print $2}')"

		if [ "$CHARSET" != utf-8 ]; then
			mv $i $i.old
	        iconv -f "$CHARSET" -t utf8 "$i.old" -o "$i"
	        echo "convet $i\n"
	    else
	    	echo "$i is alredy utf8 file"
		fi
    fi   
    if [ -d $1$i ]; then
    	echo "run on new dir $1$i"
    	`$0 $1$i`

    fi

done