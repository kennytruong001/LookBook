class CustomerDAO:
    """Customer Data Access Object.

    Responsible for low level database operations for User.
    Below are accessible fields in each MongoDB document.
    """
    ID = "_id"
    USERNAME = "username"
    FIRST_NAME = "first_name"
    LAST_NAME = "last_name"
    PASSWORD = "password"
    EMAIL = "email"
    PHONE_NUMBER = "phone_number"
    CREATE_DATE = "create_date"
    UPDATE_DATE = "update_date" 
    ATTRIBUTES = [ID, USERNAME, FIRST_NAME, LAST_NAME, PASSWORD, EMAIL, PHONE_NUMBER, CREATE_DATE, UPDATE_DATE]


    def __init__(self):
        """Initializes Button DAO."""
        self.collection: Collection = None


    def init_app(self, app: Flask, mongo_client: Mongo):
        """Initializes with a flask app and shared mongo client connection.

        Args:
            app (Flask): flask app reference
            mongo_client (Mongo): mongo connection shared across DAOs
        """
        self.collection = mongo_client.database.get_collection(constants.MONGO_BUTTON_COLLECTION)


    def get_user_by_id(self, id: str) -> Optional[User]:
        """Queries for button by id.

        Args:
            id (str): button id

        Returns:
            Optional[Button]: Button returned from query
        """
        query = {ButtonDAO.ID: id}
        try:
            result = self.collection.find_one(query)
        except Exception as e:
            print("get_button_by_id exception: ", e.__str__)
            return None
        if not result:
            return None
        return Button.from_dict(result, ButtonDAO.ATTRIBUTES)


    def get_all_buttons(self) -> List[Button]:
        """Queries for all buttons

        Returns:
            List[Button]: List of all buttons
        """
        try:
            result: Cursor = self.collection.find()
        except Exception as e: 
            print("get_all_buttons exception: {e.__str__}")
            return []
        button_list = [Button.from_dict(button_dict, ButtonDAO.ATTRIBUTES) for button_dict in result]
        return button_list


    def insert_button(self, button: Button) -> Optional[Button]:
        """Inserts a new button into the database.

        Args:
            button (Button): button to insert

        Returns:
            Optional[Button]: updated button with new generated id
        """
        data = button.to_dict(ButtonDAO.ATTRIBUTES)
        try:
            result: InsertOneResult = self.collection.insert_one(data)
        except Exception as e:
            print("insert_button exception: ", e.__str__)
            return None
        finally: 
            return Button(
            id = str(result.inserted_id),
            count = button.count,
            create_date = button.create_date,
            update_date = button.update_date
            )


    def increment_button_counter(self, id: str) -> Optional[Button]:
        """Increments an existing button counter by 1 in MongoDB.

        Args:
            id (str): button id

        Returns:
            Optional[Button]: Result button if found
        """
        query = {ButtonDAO.ID: id}
        update = {
            '$inc': {ButtonDAO.COUNT: 1},
            '$set': {ButtonDAO.UPDATE_DATE: datetime.utcnow()}
        }  
        try:
            result: dict = self.collection.find_one_and_update(
            query,
            update,
            return_document=ReturnDocument.AFTER
            )
        except Exception as e:
            print(f"increment_button_counter exception: {e.__str__}")
            return None
        if not result:
            return None
        return Button.from_dict(result, ButtonDAO.ATTRIBUTES)


    def reset_button_counter(self, id: str) -> Optional[Button]:
        """Resets button counter to 0.

        Args:
            id (str): id of button

        Returns:
            Optional[Button]: button with reset counter if id matched
        """
        query = {ButtonDAO.ID: id}
        update = {
            "$set": {
            ButtonDAO.COUNT: 0,
            ButtonDAO.UPDATE_DATE: datetime.utcnow()
            }
        }
        try:
            result: dict = self.collection.find_one_and_update(
            query,
            update,
            return_document=ReturnDocument.AFTER
            )
        except Exception as e:
            print(f"reset_button_counter exception: {e.__str__}")
            return None
        if not result:
            return None
        return Button.from_dict(result, ButtonDAO.ATTRIBUTES)


    def delete_button(self, id: str) -> Optional[Button]:
        """Deletes existing button.

        Args:
            id (str): button id

        Returns:
            Optional[Button]: deleted button
        """
        query = {ButtonDAO.ID: id}
        try:
            result: dict = self.collection.find_one_and_delete(query)
        except Exception as e:
            print(f"delete_button exception: {e.__str__}")
            return None
        if not result:
            return None
        return Button.from_dict(result, ButtonDAO.ATTRIBUTES)
  
def confirm(appointment):
    if appointment:
        pass
    
def reject(appointment):
    if appointment:
        pass

def edit_availbility(availbility):
    pass