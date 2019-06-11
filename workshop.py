Welcome to Canopy's interactive data-analysis environment!

Kernel running in the 'User' environment.

Pylab is active using Qt4Agg.

Python 3.5.2 |Enthought, Inc. (x86_64)| (default, Mar  2 2017, 16:37:47) [MSC v.1900 64 bit (AMD64)]
Type "copyright", "credits" or "license" for more information.

IPython 5.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.

%run "F:\numpy_speed.py"
  File "F:\numpy_speed.py", line 6
    %timeit sqr(t)
    ^
SyntaxError: invalid syntax 

%run -i "F:\numpy_speed.py"
  File "F:\numpy_speed.py", line 6
    %timeit sqr(t)
    ^
SyntaxError: invalid syntax 

%run "F:\numpy_speed.py"

%run "F:\numpy_speed.py"
[      0       1       2 ..., 9999997 9999998 9999999]

%run -i "F:\numpy_speed.py"
[      0       1       2 ..., 9999997 9999998 9999999]

%run "F:/numpy_array.py"
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
F:\numpy_array.py in <module>()
      2 from pylab import*
      3 x = linspace(0,1)
----> 4 x = numpy.linspace(0,1)
      5 plot(x,sin(x))
      6 show()
NameError: name 'numpy' is not defined 

%run "F:/numpy_array.py"
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
F:\numpy_array.py in <module>()
      2 from pylab import*
      3 x = linspace(0,1)
----> 4 x = numpy.linspace(0,1)
      5 plot(x,sin(x))
      6 show()
NameError: name 'numpy' is not defined 

%run "F:/numpy_array.py"
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
F:\numpy_array.py in <module>()
      2 from pylab import*
      3 x = linspace(0,1)
----> 4 x = numpy.linspace(0,1)
      5 plot(x,sin(x))
      6 show()
NameError: name 'numpy' is not defined 

%run -i "F:/numpy_array.py"
1 4
[3 5 7 9] [-1 -1 -1 -1] [ 0.5         0.66666667  0.75        0.8       ]

%run "F:/numpy_array.py"
  File "F:\numpy_array.py", line 18
    x[0]=-1
    ^
SyntaxError: invalid syntax 

%run "F:/numpy_array.py"
  File "F:\numpy_array.py", line 18
    x[0]=-1
    ^
SyntaxError: invalid syntax 

%run "F:/numpy_array.py"
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
F:\numpy_array.py in <module>()
      2 from pylab import*
      3 x = linspace(0,1)
----> 4 x = numpy.linspace(0,1)
      5 plot(x,sin(x))
      6 show()
NameError: name 'numpy' is not defined 

%run "F:/numpy_array.py"
1 4
[3 5 7 9] [-1 -1 -1 -1] [ 0.5         0.66666667  0.75        0.8       ]
-1.0 6.28318530718

%run "F:/numpy_array.py"
1 4
[3 5 7 9] [-1 -1 -1 -1] [ 0.5         0.66666667  0.75        0.8       ]
-1.0 6.28318530718

%run -i "F:/numpy_array.py"
1 4
[3 5 7 9] [-1 -1 -1 -1] [ 0.5         0.66666667  0.75        0.8       ]
-1.0 6.28318530718
4

%run -i "F:/numpy_array.py"
1 4
[3 5 7 9] [-1 -1 -1 -1] [ 0.5         0.66666667  0.75        0.8       ]
-1.0 6.28318530718
4
float64
(4,)
1
F:/numpy_array.py:25: VisibleDeprecationWarning: `rank` is deprecated; use the `ndim` attribute or function instead. To find the rank of a matrix see `numpy.linalg.matrix_rank`.
  print(rank(x))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
F:/numpy_array.py in <module>()
     24 print(x.shape)
     25 print(rank(x))
---> 26 print(x.itemSize)

AttributeError: 'numpy.ndarray' object has no attribute 'itemSize' 

%run "F:/numpy_array.py"
1 4
[3 5 7 9] [-1 -1 -1 -1] [ 0.5         0.66666667  0.75        0.8       ]
-1.0 6.28318530718
4
float64
(4,)
1
F:\numpy_array.py:25: VisibleDeprecationWarning: `rank` is deprecated; use the `ndim` attribute or function instead. To find the rank of a matrix see `numpy.linalg.matrix_rank`.
  print(rank(x))
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
F:\numpy_array.py in <module>()
     24 print(x.shape)
     25 print(rank(x))
---> 26 print(x.itemSize)
     27 
     28 #multidimensional array
AttributeError: 'numpy.ndarray' object has no attribute 'itemSize' 

%run -i "F:/numpy_array.py"
1 4
[3 5 7 9] [-1 -1 -1 -1] [ 0.5         0.66666667  0.75        0.8       ]
-1.0 6.28318530718
4
float64
(4,)
1
8
F:/numpy_array.py:25: VisibleDeprecationWarning: `rank` is deprecated; use the `ndim` attribute or function instead. To find the rank of a matrix see `numpy.linalg.matrix_rank`.
  print(rank(x))

%run -i "F:/numpy_array.py"
1 4
[3 5 7 9] [-1 -1 -1 -1] [ 0.5         0.66666667  0.75        0.8       ]
-1.0 6.28318530718
4
float64
(4,)
1
8
F:/numpy_array.py:25: VisibleDeprecationWarning: `rank` is deprecated; use the `ndim` attribute or function instead. To find the rank of a matrix see `numpy.linalg.matrix_rank`.
  print(rank(x))

a = array([[1,2,3],[4,5,6],[7,8,9]])

a[0::2,0::2]
Out[90]: 
array([[1, 3],
       [7, 9]])

a = array([1,2,3],dtype=float)

ones_like(a)
Out[92]: array([ 1.,  1.,  1.])

ones(2,3))
  File "<ipython-input-93-bd9512fa073a>", line 1
    ones(2,3))
             ^
SyntaxError: invalid syntax 

ones((2,3))
Out[94]: 
array([[ 1.,  1.,  1.],
       [ 1.,  1.,  1.]])

import numpy

numpy.
  File "<ipython-input-96-08f379dd8eec>", line 1
    numpy.
          ^
SyntaxError: invalid syntax 

x = loadtxt('pendulum.txt')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
F:/numpy_array.py in <module>()
----> 1 x = loadtxt('pendulum.txt')

C:\Users\Lenovo\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\numpy\lib\npyio.py in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin)
    896                 fh = iter(open(fname, 'U'))
    897             else:
--> 898                 fh = iter(open(fname))
    899         else:
    900             fh = iter(fname)
FileNotFoundError: [Errno 2] No such file or directory: 'pendulum.txt' 

x.shape
Out[98]: (4,)

x,y=loadtxt('pendulum.txt',unpack=True)
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
F:/numpy_array.py in <module>()
----> 1 x,y=loadtxt('pendulum.txt',unpack=True)

C:\Users\Lenovo\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\numpy\lib\npyio.py in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin)
    896                 fh = iter(open(fname, 'U'))
    897             else:
--> 898                 fh = iter(open(fname))
    899         else:
    900             fh = iter(fname)
FileNotFoundError: [Errno 2] No such file or directory: 'pendulum.txt' 

x = loadtxt('pendulum.txt')
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
F:/numpy_array.py in <module>()
----> 1 x = loadtxt('pendulum.txt')

C:\Users\Lenovo\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\numpy\lib\npyio.py in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin)
    896                 fh = iter(open(fname, 'U'))
    897             else:
--> 898                 fh = iter(open(fname))
    899         else:
    900             fh = iter(fname)
FileNotFoundError: [Errno 2] No such file or directory: 'pendulum.txt' 

%run -i "F:/numpy_array.py"
1 4
[3 5 7 9] [-1 -1 -1 -1] [ 0.5         0.66666667  0.75        0.8       ]
-1.0 6.28318530718
4
float64
(4,)
1
8
F:/numpy_array.py:25: VisibleDeprecationWarning: `rank` is deprecated; use the `ndim` attribute or function instead. To find the rank of a matrix see `numpy.linalg.matrix_rank`.
  print(rank(x))
---------------------------------------------------------------------------
FileNotFoundError                         Traceback (most recent call last)
F:/numpy_array.py in <module>()
     34 a[1]=0
     35 
---> 36 x = loadtxt('pendulum.txt')
     37 x.shape
C:\Users\Lenovo\AppData\Local\Enthought\Canopy\edm\envs\User\lib\site-packages\numpy\lib\npyio.py in loadtxt(fname, dtype, comments, delimiter, converters, skiprows, usecols, unpack, ndmin)
    896                 fh = iter(open(fname, 'U'))
    897             else:
--> 898                 fh = iter(open(fname))
    899         else:
    900             fh = iter(fname)
FileNotFoundError: [Errno 2] No such file or directory: 'pendulum.txt' 

pwd
Out[102]: 'C:\\Users\\Lenovo'

ls
 Volume in drive C has no label.
 Volume Serial Number is 4AA4-6053

 Directory of C:\Users\Lenovo

06/06/2019  12:22 PM    <DIR>          .
06/06/2019  12:22 PM    <DIR>          ..
05/01/2018  10:04 AM               145 .appletviewer
27/01/2018  12:23 AM    <DIR>          .argouml
06/06/2019  08:51 AM               185 .canopy_runtimes.json
20/02/2019  01:11 PM    <DIR>          .eclipse
10/03/2018  07:47 AM    <DIR>          .idlerc
06/06/2019  08:42 AM    <DIR>          .ipython
16/10/2018  08:16 PM                91 .irbrc
06/06/2019  08:51 AM    <DIR>          .jupyter
06/06/2019  12:13 PM    <DIR>          .matplotlib
23/04/2019  01:18 AM    <DIR>          .nbi
23/04/2019  01:02 AM    <DIR>          .netbeans-derby
17/05/2019  12:58 PM    <DIR>          .p2
13/03/2018  05:06 PM    <DIR>          .PyCharmCE2016.3
19/04/2019  12:23 PM    <DIR>          .VirtualBox
04/01/2018  02:22 PM    <DIR>          3D Objects
06/06/2019  08:42 AM    <DIR>          Canopy
04/01/2018  02:22 PM    <DIR>          Contacts
06/06/2019  11:40 AM    <DIR>          Desktop
06/06/2019  08:33 AM    <DIR>          Documents
06/06/2019  08:56 AM    <DIR>          Downloads
04/01/2018  02:22 PM    <DIR>          Favorites
06/06/2019  12:22 PM            52,297 four.png
02/05/2018  06:06 PM    <DIR>          Links
04/01/2018  02:22 PM    <DIR>          Music
19/09/2011  08:25 PM            49,152 NPProt.bkp
19/09/2011  08:25 PM            49,152 NPProt.exe
29/04/2019  06:33 PM    <DIR>          OneDrive
25/02/2019  01:30 PM    <DIR>          Pictures
04/01/2018  02:22 PM    <DIR>          Saved Games
04/01/2018  02:22 PM    <DIR>          Searches
04/01/2018  04:11 PM    <DIR>          temp
12/02/2018  04:40 PM    <DIR>          Videos
04/01/2018  04:44 PM    <DIR>          VirtualBox VMs
30/10/2018  12:11 AM    <DIR>          website
               6 File(s)        151,022 bytes
              30 Dir(s)  15,676,448,768 bytes free

cd
C:\Users\Lenovo

%cd "F:\"
F:\

x = loadtxt('pendulum.txt')

x
Out[107]: 
array([[ 0.1    ,  0.69004],
       [ 0.11   ,  0.69497],
       [ 0.12   ,  0.74252],
       [ 0.13   ,  0.7536 ],
       [ 0.14   ,  0.83568],
       [ 0.15   ,  0.86789],
       [ 0.16   ,  0.84182],
       [ 0.17   ,  0.85379],
       [ 0.18   ,  0.85762],
       [ 0.19   ,  0.8839 ],
       [ 0.2    ,  0.89985],
       [ 0.21   ,  0.98436],
       [ 0.22   ,  1.0244 ],
       [ 0.23   ,  1.0572 ],
       [ 0.24   ,  0.99077],
       [ 0.25   ,  1.0058 ],
       [ 0.26   ,  1.0727 ],
       [ 0.27   ,  1.0943 ],
       [ 0.28   ,  1.1432 ],
       [ 0.29   ,  1.1045 ],
       [ 0.3    ,  1.1867 ],
       [ 0.31   ,  1.1385 ],
       [ 0.32   ,  1.2245 ],
       [ 0.33   ,  1.2406 ],
       [ 0.34   ,  1.2071 ],
       [ 0.35   ,  1.2658 ],
       [ 0.36   ,  1.2995 ],
       [ 0.37   ,  1.3142 ],
       [ 0.38   ,  1.2663 ],
       [ 0.39   ,  1.2578 ],
       [ 0.4    ,  1.2991 ],
       [ 0.41   ,  1.3058 ],
       [ 0.42   ,  1.3478 ],
       [ 0.43   ,  1.3506 ],
       [ 0.44   ,  1.4044 ],
       [ 0.45   ,  1.3948 ],
       [ 0.46   ,  1.38   ],
       [ 0.47   ,  1.448  ],
       [ 0.48   ,  1.4168 ],
       [ 0.49   ,  1.4719 ],
       [ 0.5    ,  1.4656 ],
       [ 0.51   ,  1.4399 ],
       [ 0.52   ,  1.5174 ],
       [ 0.53   ,  1.4988 ],
       [ 0.54   ,  1.4751 ],
       [ 0.55   ,  1.5326 ],
       [ 0.56   ,  1.5297 ],
       [ 0.57   ,  1.5372 ],
       [ 0.58   ,  1.6094 ],
       [ 0.59   ,  1.6352 ],
       [ 0.6    ,  1.5843 ],
       [ 0.61   ,  1.6643 ],
       [ 0.62   ,  1.5987 ],
       [ 0.63   ,  1.6585 ],
       [ 0.64   ,  1.6317 ],
       [ 0.65   ,  1.7074 ],
       [ 0.66   ,  1.6654 ],
       [ 0.67   ,  1.6551 ],
       [ 0.68   ,  1.6964 ],
       [ 0.69   ,  1.7143 ],
       [ 0.7    ,  1.7706 ],
       [ 0.71   ,  1.7622 ],
       [ 0.72   ,  1.726  ],
       [ 0.73   ,  1.8089 ],
       [ 0.74   ,  1.7905 ],
       [ 0.75   ,  1.7428 ],
       [ 0.76   ,  1.8381 ],
       [ 0.77   ,  1.8182 ],
       [ 0.78   ,  1.7865 ],
       [ 0.79   ,  1.7995 ],
       [ 0.8    ,  1.8296 ],
       [ 0.81   ,  1.8625 ],
       [ 0.82   ,  1.8623 ],
       [ 0.83   ,  1.8383 ],
       [ 0.84   ,  1.8593 ],
       [ 0.85   ,  1.8944 ],
       [ 0.86   ,  1.9598 ],
       [ 0.87   ,  1.9    ],
       [ 0.88   ,  1.9244 ],
       [ 0.89   ,  1.9397 ],
       [ 0.9    ,  1.944  ],
       [ 0.91   ,  1.9718 ],
       [ 0.92   ,  1.9383 ],
       [ 0.93   ,  1.9555 ],
       [ 0.94   ,  2.0006 ],
       [ 0.95   ,  1.9841 ],
       [ 0.96   ,  2.0066 ],
       [ 0.97   ,  2.0493 ],
       [ 0.98   ,  2.0503 ],
       [ 0.99   ,  2.0214 ]])

x,y=loadtxt('pendulum.txt',unpack=True)

x.shape
Out[109]: (90,)

cat pendulum.txt
  File "<ipython-input-110-7c8ac3036ddd>", line 1
    cat pendulum.txt
               ^
SyntaxError: invalid syntax 

!ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

x,y=loadtxt('pendulum.txt',unpack=True)

plot(x,y,--)
  File "<ipython-input-113-cc77c749c503>", line 1
    plot(x,y,--)
               ^
SyntaxError: invalid syntax 

plot(x,y,'--')
Out[114]: [<matplotlib.lines.Line2D at 0x1d000033550>]

show()

L,t = x[:,0]x[:,1]
  File "<ipython-input-116-daeac4b09fff>", line 1
    L,t = x[:,0]x[:,1]
                ^
SyntaxError: invalid syntax 

L,t = x[:,0],x[:,1]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
F:/numpy_array.py in <module>()
----> 1 L,t = x[:,0],x[:,1]

IndexError: too many indices for array 
