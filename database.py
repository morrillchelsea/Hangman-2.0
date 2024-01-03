def create_table():
    return


    ''' class to manage DynamoDB objects and methods '''
    # class variables
    resc = boto3.resource('dynamodb')
    #declareboto3 client instance
    client = boto3.client('dynamodb')
    table_name = 'Leaderboard'
    # define table
    table = resc.Table(table_name)

    def add_items(self, initials, score):
        ''' Method to input data to table Statistics '''
        # scan number of items currently in DynamoDB
        scan_items = self.table.scan()
        # assign num of items in table to items var
        items = len(scan_items['Items'])
        # add to num of items to increment userid key
        incr_userid = items + 1
        # assign incremented key to userid var 
        userid = incr_userid

        try:
            # put_item request to add item to dynamodb
            self.table.put_item(
                Item={
                    'UserID' : userid,
                    'Initials': initials,
                    'Score': score
                    #'Rank': rank
                }
            )
        except ClientError as err:
            logging.error(
                "Couldn't add initials %s to table %s. Here's why: %s: %s",
                initials, self.table.name,
                err.response['Error']['Code'], err.response['Error']['Message'])
            raise

    def view_my_stats(self, initials):
        ''' method to handle viewing user's game score history '''
        #while selection_handler():
        #display program title
        print('\nLeaderboard\n')

        #scan items in dynamodb table
        response = self.client.scan(
            TableName= self.table_name, #assign table name filter to scan
            FilterExpression='Initials = :initials',
            ExpressionAttributeValues={
                ':initials': {'S': f'{initials}'}
            }
        )
        #if items not in response
        if response['Count'] == 0:
            #output leaderboard item not found
            print('\nNo data in leaderboard')
            print('You have not played any games\n')
        else:
            for i in response['Items']:
                print({'Initials': i['Initials'], 'Score': i['Score']}, '\n')

    def view_leaderboard(self):
        ''' method to output top 5 scores from leaderboard to user '''
        return

    def create_table(self):
        '''Using the AWS SDK and Python within your AWS Educate Cloud9 environment, create a
        DynamoDB table'''

        # call create_table operation to add table to db
        try:
            new_table = self.resc.create_table(
                #Assign name 'Courses' to table
                TableName= self.table_name,
                KeySchema=[
                    {
                        'AttributeName': 'UserID', #Name of attribute to be assigned as PK
                        'KeyType': 'HASH'#Assign keytype HASH to Attribute CourseID
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName' : 'UserID', #Assign name to PK
                        'AttributeType' : 'N' #Assign data type number to PK
                    }
                ],
                ProvisionedThroughput={
                    #The maximum number of strongly consistent reads consumed per second
                    #before DynamoDB returns a ThrottlingException
                    'ReadCapacityUnits': 5, 
                    #The maximum number of writes consumed per second
                    #before DynamoDB returns a ThrottlingException
                    'WriteCapacityUnits': 5
                }
            )
            print('Table status:', new_table.table_status) #Output table creation status
            #set up waiter to wait until table exists to put items
            waiter = self.client.get_waiter('table_exists')
            waiter.wait(
                TableName=self.table_name,
                WaiterConfig={
                    'Delay': 20,
                    'MaxAttempts': 25
                }
            )
        except self.client.exceptions.ResourceInUseException:
            #Output error if table already exists
            print(f'Table {self.table_name} exists.')
            return False
        return True
