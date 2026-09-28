#include <iostream>
#include <fstream>
#include <vector>

static bool load_file_bytes(const char* path, unsigned char* headers, const int size) {
    std::ifstream file(path, std::ios::binary);
    if (!file) { return false; }
    file.read(reinterpret_cast<char*>(headers), size);
    return true;
}

// Собирает 2 или 4 байта в число 
static int read2(const unsigned char* b, int pos) {
    return b[pos] | (b[pos + 1] << 8);
}
static int read4(const unsigned char* b, int pos) {
    return b[pos] | (b[pos + 1] << 8) | (b[pos + 2] << 16) | (b[pos + 3] << 24);
}

int main(const int argc, char** argv) {
    const char* path = argc > 1 ? argv[1] : "lena.bmp";

    // 1. Читаем только заголовок (54 байта)
    unsigned char buffer[54]{};
    if (!load_file_bytes(path, buffer, 54)) {
        std::cerr << "Cant load file" << std::endl;
        return 1;
    }
    if (buffer[0] != 'B' || buffer[1] != 'M') {
        std::cerr << "Not a BMP file" << std::endl;
        return 1;
    }

    int file_size        = read4(buffer, 2);
    int data_offset      = read4(buffer, 10);
    int info_size        = read4(buffer, 14);
    int width            = read4(buffer, 18);
    int height           = read4(buffer, 22);
    int planes           = read2(buffer, 26);
    int bitcount         = read2(buffer, 28);
    int compression      = read4(buffer, 30);
    int imgsize          = read4(buffer, 34);
    int xpix             = read4(buffer, 38);
    int ypix             = read4(buffer, 42);
    int colorsused       = read4(buffer, 46);
    int colorsimportant  = read4(buffer, 50);

    std::cout << "2b headers.bitmap_signature : " << buffer[0] << buffer[1] << '\n';
    std::cout << "4b headers.bitmap_file_size : " << file_size << '\n';
    std::cout << "4b headers.bitmap_data_offset : " << data_offset << '\n';
    std::cout << "4b headers.bitmap_info_header_size : " << info_size << '\n';
    std::cout << "4b headers.bitmap_width : " << width << '\n';
    std::cout << "4b headers.bitmap_height : " << height << '\n';
    std::cout << "2b headers.bitmap_planes : " << planes << '\n';
    std::cout << "2b headers.bitmap_bits_per_pixel : " << bitcount << '\n';
    std::cout << "4b headers.bitmap_compression : " << compression << '\n';
    std::cout << "4b headers.bitmap_image_size : " << imgsize << '\n';
    std::cout << "4b headers.bitmap_XpixelsPerM : " << xpix << '\n';
    std::cout << "4b headers.bitmap_YpixelsPerM : " << ypix << '\n';
    std::cout << "4b headers.bitmap_ColorsUsed : " << colorsused << '\n';
    std::cout << "4b headers.bitmap_ColorsImportant : " << colorsimportant << '\n';

   