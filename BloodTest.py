class BloodTest:
    """
    A class for storing test results and personal data

    ...

    Attributes
    ----------
    :param f_name : str
        first name of the person
    :param l_name : str
        second name of the person
    :param pesel : int
        pesel of the person
    :param erythrocytes : int
        number of erythrocytes
    :param leukocytes : int
        number of leukocytes
    :param platelets : int
        number of platelets
    """
    def __init__(self, f_name, l_name, pesel, erythrocytes, leukocytes, platelets):
        """
        Constructs all the necessary attributes for the BloodTest object.

        :param f_name : str
            first name of the person
        :param l_name : str
            second name of the person
        :param pesel : int
            pesel of the person
        :param erythrocytes : int
            number of erythrocytes
        :param leukocytes : int
            number of leukocytes
        :param platelets : int
            number of platelets
        """
        self.first_name = f_name
        self.last_name = l_name
        self.pesel_nr = pesel
        self.erythrocytes_nr = erythrocytes
        self.leukocytes_nr = leukocytes
        self.platelets_nr = platelets

    def __str__(self):
        """
        A method that allows to write arguments to the screen
        :return: All arguments as a string
        """
        return (f"{self.pesel_nr} "
                f"{self.first_name} "
                f"{self.last_name} "
                f"{self.erythrocytes_nr} "
                f"{self.leukocytes_nr} "
                f"{self.platelets_nr}")


