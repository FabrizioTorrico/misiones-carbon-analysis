"""File to storage all constants used in the project."""

import os

PATH_SRC = os.path.dirname(__file__)


def get_gfw_data(*args):
    return os.path.join(PATH_SRC, "..", "raw_data", *args)


def get_mapbiomas_data(**args):
    return os.path.join(PATH_SRC, "..", "raw_data", *args)


PROVINCE_SHAPE_PATH = os.path.join(
    PATH_SRC, "raw_data", "shapes", "provincia.shp"
)
ARGENTINA_TIFF_PATH = os.path.join(
    PATH_SRC, "raw_data", "argentina_coverage_2022.tif"
)
MISIONES_COVER_TIFF_PATH = os.path.join(
    PATH_SRC, "raw_data", "gfw", "Misiones_Forest_Cover.tif"
)
MISIONES_GAIN_TIFF_PATH = os.path.join(
    PATH_SRC, "raw_data", "gfw", "Misiones_Forest_Gain.tif"
)
MISIONES_LOSS_TIFF_PATH = os.path.join(
    PATH_SRC, "raw_data", "gfw", "Misiones_Forest_Loss.tif"
)
