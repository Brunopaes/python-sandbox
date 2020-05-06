from pdf2image import convert_from_path
from tqdm import tqdm

import os


class PDF2Image:
    """Class for converting PDF files into images.

    Can handle entire files or specific pages - just pass it as an argument.

    Parameters
    ----------
    pdf_path : str
        Path to PDF file.
    output_path : str
        Output Directory.
    first_page : int, optional
        Page range beginning.
    last_page : int, optional
        Page range ending.
    dpi : int, optional
        Converted image resolution.
    poppler : str, optional
        Python's library for PDF rendering path.

    >>> from pdf_converter import PDF2Image
    >>> PDF2Image('path/to/pdf', 'path/to/output').__call__()

    """
    def __init__(self, pdf_path, output_path, first_page=None, last_page=None,
                 dpi=500, poppler='../../data/poppler-0.68.0/bin'):
        self.pdf_path = pdf_path
        self.output_path = output_path
        self.first_page = first_page
        self.last_page = last_page
        self.dpi = dpi
        self.poppler = poppler

    # Used in __call__
    def getting_basename(self):
        """This method gets the PDF's file basename, lowers it and joins by -.

        Returns
        -------
        self.basename : str
            The PDF's file formatted basename.

        """
        return '-'.join(os.path.splitext(os.path.basename(
            self.pdf_path))[0].lower().split(' '))

    # Used in __call__
    def formatting_output_path(self):
        """This function formats the output's path.

        Returns
        -------
        self.output_path : str
            The formatted output dir path.

        """
        return os.path.abspath(os.path.join(self.output_path, self.basename))

    # Used in __call__
    def checking_directory(self):
        """This function checks if the output dir path exists. Create if not.

        Returns
        -------

        """
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    # Used in __call__
    def converting(self):
        """This function converts the n-pages PDF file into n-images.

        Returns
        -------
        pil_images : iterable
            A list containing n-PIL objects.

        """
        if (self.first_page is None) or (self.last_page is None):
            return convert_from_path(
                self.pdf_path,
                poppler_path=self.poppler,
                dpi=self.dpi
            )
        else:
            return convert_from_path(
                self.pdf_path,
                poppler_path=self.poppler,
                first_page=self.first_page,
                last_page=self.last_page,
                dpi=self.dpi
            )

    # Used in __call__
    def saving_files(self):
        """This function saves the files into the desired output dir.

        Returns
        -------

        """
        filepath = self.basename + '-{}.jpg'
        for idx, page in tqdm(enumerate(self.images), total=len(self.images)):
            page.save(os.path.join(self.output_path, filepath.format(idx)),
                      'JPEG')

    def __call__(self, *args, **kwargs):
        self.basename = self.getting_basename()
        self.output_path = self.formatting_output_path()
        self.checking_directory()
        self.images = self.converting()
        self.saving_files()


if __name__ == '__main__':
    PDF2Image(
        r"C:\Users\bruno\Desktop\Sarah Nowak.pdf",
        r"C:\Users\bruno\Desktop",
        950
    ).__call__()

