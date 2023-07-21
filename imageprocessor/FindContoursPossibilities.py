import cv2


class FindContoursMethodsPossibilities:
    retr_methods = {
        'RETR_EXTERNAL': cv2.RETR_EXTERNAL,
        'RETR_LIST': cv2.RETR_LIST,
        'RETR_CCOMP': cv2.RETR_CCOMP,
        'RETR_TREE': cv2.RETR_TREE
    }

    approx_methods = {
        'CHAIN_APPROX_SIMPLE': cv2.CHAIN_APPROX_SIMPLE,
        'CHAIN_APPROX_NONE': cv2.CHAIN_APPROX_NONE
    }