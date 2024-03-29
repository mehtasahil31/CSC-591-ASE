from boot import *
#
# def last(arr):
#     "Returns last element from given list"
#     return arr[-1]
#
#
# def first(arr):
#     "Returns first element from given list"
#     return arr[0]
#
#
# def same(num):
#     "Right now returns same number"
#     return num
#
#
# def ordered(num_list, key, index):
#     "Sort elements in array at the same time ignore 'Skip' characters"
#     return sorted(num_list, key=lambda x: x[index])


# class DIVISION_UTILS:
#     trivial = 1.025
#     cohen = 0.3
#     minimum = 0.5
#     minObs = 4


THE = o(
    char=o(sep=",",
           num="$",
           less="<",
           more=">",
           skip="?",
           klass="!",
           doomed=r'([\n\t\r ]|#.*)'),
    div=o(trivial=1.025,
          cohen=0.3,
          min=0.5),
    tree=o(minObs=4,
           trivial=1.025,
           minimum=0.5,
           cohen=0.3,
           rnd=1)
)
