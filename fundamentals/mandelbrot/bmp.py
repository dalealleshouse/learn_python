#!/usr/bin/env python3
"""A module for deailing with BMP bitmap image files."""


def write_greyscale(filename, pixels):
    """Create and write a grayscale BMP file.

    Args:
        filename: The name of the BMP file to be created.

        pixels: A rectangular image stored as a sequence of rows.
        Each row much be an interable series of integers in the
        range 1-255.

    Raises:
        OSError: If the file couldn't be written.

    """
    height = len(pixels)
    width = len(pixels[0])

    # 'wb' - write, binary
    with open(filename, 'wb') as bmp:
        # BMP Header
        bmp.write(b'BM')

        # The next four bytes hold teh fileszie as a 32-bit
        size_bookmark = bmp.tell()
        # little-endian intger. Zero placehold for now
        bmp.write(b'\x00\x00\x00\x00')

        bmp.write(b'\x00\x00')  # unused 16-bit integer - should be zero
        bmp.write(b'\x00\x00')  # unused 16-bit integer - should be zero

        # The next four bytes hold the intger offset
        pixel_offset_bookmark = bmp.tell()
        # to the pixel data. Zero placeholder for now
        bmp.write(b'\x00\x00\x00\x00')

        # Image Header
        # Image header size in bytes - 40 decimal
        bmp.write(b'\x28\x00\x00\x00')
        bmp.write(_int32_to_bytes(width))  # Image width in pixels
        bmp.write(_int32_to_bytes(height))  # Image height in pixels
        bmp.write(b'\x01\x00')  # Number of image planes
        bmp.write(b'\x08\x00')  # Bits per pixel 8 for greyscale
        bmp.write(b'\x00\x00\x00\x00')  # No compression
        bmp.write(b'\x00\x00\x00\x00')  # Zero for uncompressed images
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per meter
        bmp.write(b'\x00\x00\x00\x00')  # Unused pixels per metere
        bmp.write(b'\x00\x00\x00\x00')  # Use whole color table
        bmp.write(b'\x00\x00\x00\x00')  # All colors are important

        # Color paletter - a linear greyscale
        for c in range(256):
            bmp.write(bytes((c, c, c, 0)))  # Blue, Green, Red, Zero

        # Pixel data
        pixel_data_bookmark = bmp.tell()
        for row in reversed(pixels):
            row_data = bytes(row)
            bmp.write(row_data)
            padding = b'\x00' * (4 - (len(row) % 4))
            bmp.write(padding)

        # End of file
        eof_bookmark = bmp.tell()

        # Fill in the file size placeholder
        bmp.seek(size_bookmark)
        bmp.write(_int32_to_bytes(eof_bookmark))

        # Fill in the pixel offset placeholder
        bmp.seek(pixel_offset_bookmark)
        bmp.write(_int32_to_bytes(pixel_data_bookmark))


def _int32_to_bytes(i):
    """Convert an integer to four bytes in little-endian format."""
    return bytes((i & 0xff,
                  i >> 8 & 0xff,
                  i >> 16 & 0xff,
                  i >> 24 & 0xff))


def dimensions(filename):
    """Determine the dimensions in pixels of a BMP image.

    Args:
        filename: The filename of the BMP file.

    Returns:
        A tuple containing two integers with the width
        and height in pixels.

    Raises:
        ValueError: If the file was not a BMP file.
        OSError: If there was a problem reading the file.

    """
    with open(filename, 'rb') as f:
        magic = f.read(2)
        if magic != b'BM':
            raise ValueError("{} is not a BMP file.".format(filename))

        f.seek(18)
        width_bytes = f.read(4)
        height_bytes = f.read(4)

        return (_bytes_to_int32(width_bytes),
                _bytes_to_int32(height_bytes))


def _bytes_to_int32(b):
    """Convert a bytes object containing four bytes into an integer."""
    return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24)
