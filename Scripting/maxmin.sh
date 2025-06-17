min2(){
    echo 'arg1 (min2): ' $1
    echo 'arg2 (min2): ' $2
    if (($1 < $2))
    then
        echo $1
    else
        echo $2
    fi
}

max2(){
    echo 'arg1 (max2): ' $1
    echo 'arg2 (max2): ' $2
    if (($1 > $2))
    then
        echo $1
    else
        echo $2
    fi
}

max2 $3 $4
min2 $1 $2
