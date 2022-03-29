# yuv_to_y4m
Convert .yuv files to .y4m format with python

## YUV to Y4M flags ##

Example command:

```
yuv_to_y4m.py -i /path/to/file.yuv -o output.y4m -w 480 -e 270 -n 60 -d 1 -f Ip -C 420jpeg
```

Parameters list
- -w : width
- -e : height
- -n : numerator of framerate
- -d : denominator of framerate
- -f : interlacing
- -C : colourspace

## Help ##

For additional info on options: [YUV4MPEG2]


[YUV4MPEG2]:https://wiki.multimedia.cx/index.php/YUV4MPEG2
