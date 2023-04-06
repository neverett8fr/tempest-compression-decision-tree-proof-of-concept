# tempest-compression-decision-tree

this isnt a hosted service, but instead the script to train a ML model (decision tree / random forest), and script to generate dataset (if one can't be found)
  
```
txt - 1
png - 2
jpg - 3

none - 0
gzip - 1
rle - 2
lzw - 3
```
  
inputs: `file_type`, `file_size` - file size does make a difference  
  
```
Compression Method: 1, File Type: 1, Predicted Ratio: 0.6359836081329736
Compression Method: 2, File Type: 1, Predicted Ratio: -0.46645259900887326
Compression Method: 3, File Type: 1, Predicted Ratio: 0.6474698081076373
  file type, best predicted method 1 3
Compression Method: 1, File Type: 2, Predicted Ratio: 0.0003519621036734682
Compression Method: 2, File Type: 2, Predicted Ratio: -0.9882352626594446
Compression Method: 3, File Type: 2, Predicted Ratio: -0.0010093792008726737
  file type, best predicted method 2 1
Compression Method: 1, File Type: 3, Predicted Ratio: 0.006286743756276049
Compression Method: 2, File Type: 3, Predicted Ratio: -0.972365365952534
Compression Method: 3, File Type: 3, Predicted Ratio: -0.004881802042100925
  file type, best predicted method 3 1
```
