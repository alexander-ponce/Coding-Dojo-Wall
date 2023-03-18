from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user
from flask import flash


class Posts:
    DB = "coding_dojo_wall"
    def __init__(self, data):
        self.id = data['id']
        self.user_id = data['user_id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.creator = None

    @classmethod
    def save_post(cls, data):
        # if not cls.validate_post(data):
        #     return False

        query= '''
                INSERT INTO Posts (user_id, content)
                VALUES (%(user_id)s, %(content)s);
        '''
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    #NEEEEEED TO FINISH THIS SECITON =================

    @classmethod
    def get_all_post(cls):
        query= """
            SELECT * FROM Posts
            JOIN Users
            Where Posts.user_id = users.id
            ORDER BY Posts.created_at DESC;
            
            
        """
        results = connectToMySQL(cls.DB).query_db(query)
        

        all_posts = []

        for row in results:

            one_post = cls(row)
            
            user_data = {
                'id': row ['Users.id'],
                'first_name': row ['first_name'],
                'last_name': row ['last_name'],
                'email': row ['email'],
                'password': row ['password'],
                'created_at': row ['created_at'],
                'updated_at': row ['updated_at']
            }
            one_post.creator = user.Users(user_data)
            all_posts.append(one_post)
        return all_posts



    @classmethod
    def delete_post(cls, data):
            query= '''
                DELETE FROM Posts
                WHERE Posts.id=%(id)s;
            '''
            return connectToMySQL(cls.DB).query_db(query, data)

    #validating my post to make sure the textbox is not empty
    @staticmethod
    def validate_post(form_data):
            is_valid = True
            
            if len(form_data["content"]) < 1:
                flash("Post content must not be blank.")
                is_valid = False
            
            return is_valid
    #this is another way to get my flash message to display.
    # @staticmethod
    # def validate_post(form_data):
    #         is_valid = True
            
    #         if len(form_data["content"]) == 0:
    #             flash("Post cannot be empty.")
    #             is_valid = False
            
    #         return is_valid
