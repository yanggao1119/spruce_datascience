D_DATA=../data
D_CODE=../code

F_DATA_RAW=$D_DATA/spruce_data_yang.txt

tr '\r' '\n' < $F_DATA_RAW > tmp
echo >> tmp

cat tmp | python $D_CODE/get-libsvm-format.py "Run Count, Category #, Occasion, Color #, Price" "Like #" > spruce_data_yang.libsvm.all 2>spruce_data_yang.libsvm.all.log
rm tmp

#TODO: ramdomize the instances, and select a percentage of tratest instances, now hardcoding
sed 1,100!d spruce_data_yang.libsvm.all > train
sed 1,100d spruce_data_yang.libsvm.all > test

$D_CODE/libsvm-3.18/svm-train train out.model
$D_CODE/libsvm-3.18/svm-predict test out.model out.prediction
