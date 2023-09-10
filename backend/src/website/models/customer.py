class Customer():
    """Customer Model
    
    Definition of a Customer
    """

    def __init__(
            self, 
            title: str = "Customer",
            username: str = None,
            first_name: str = None,
            last_name: str = None,
            password: str = None,
            email: str = None,
            phone_number: str = None,
            ) -> None:

            """Customer Constructor
            
            Args:
                username (str, optional): Defaults to None
                first_name (str, optional): Defaults to None
                last_name (str, optional): Defaults to None
                password (str, optional): Defaults to None
                availbility (str, optional): Defaults to None
            """
            self.username = username
            self.first_name = first_name
            self.password = password
            self.email = email
            self.phone_number = phone_number

        

    