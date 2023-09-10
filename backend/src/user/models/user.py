class User():
    """User Model
    
    Definition of a User
    """

    def __init__(
            self, 
            username: str = None,
            first_name: str = None,
            last_name: str = None,
            password: str = None,
            email: str = None,
            phone_number: str = None,
            availability: dict = {"Sunday": {}, 
                                 "Monday": {}, 
                                 "Tuesday": {}, 
                                 "Wednesday": {},
                                 "Thursday": {}, 
                                 "Friday": {}, 
                                 "Saturday": {} }) -> None:

            """User Constructor
            
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
            self.availability = availability
        

    