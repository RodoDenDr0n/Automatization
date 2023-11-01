import pandas as pd

from leocard_automatic.applications_builder import ApplicationsBuilder

from tqdm import tqdm


class Processor():

    def __init__(self):
        """
        All .csv data and paths for storing
        """
        self.data = pd.DataFrame()
        self.paths = []   # TODO: consider changing to simply storing all work in dataframe

    def _get_paths(self) -> None:
        """
        Gets path where to store applications
        and photos from one user data
        :return: str
        """
        for _, info in self.data:
            path = ...
            self.paths.append(path)

    def _process_photo(self):
        """
        Standardize photo
        :return:
        """
        pass

    def _build_applications(self):
        """
        Builds applications for each applicant
        :return:
        """
        builder = ApplicationsBuilder()
        for _, info in self.data:
            builder.feed_data(info)
            builder.build_applications()

    def feed_data(self, data) -> None:
        """
        Feeds the data to processor
        :param data:
        :return: None
        """
        self.data = data

    def run(self):
        """
        Runs the processor
        TODO: Make tqdm loader for tracking progress
        :return:
        """
        self._build_applications()
        self._process_photo()
        self._get_paths()
        pass

    def move_all(self):
        """
        Moves all the files to corresponding directories
        and clears previously stored paths
        TODO: Make tqdm loader for tracking progress
        :return:
        """
        while self.paths:
            path = self.paths.pop()


if __name__ == '__main__':
    data = pd.read_csv("applicants.csv")  # TODO: csv with people
    processor = Processor()
    processor.feed_data(data)
    processor.run()
    processor.move_all()
