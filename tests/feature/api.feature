Feature: Step arguments
    Scenario Outline: GET request
        Given the API endpoint <url>
        When I perform a GET request
        Then the response code for the GET request should be <status_code>


        Examples:
        |url                                                  | status_code|
        |https://reqres.in/api/users?page=2 | 200             |
        |https://reqres.in/api/users/2            | 200             |
        |https://reqres.in/api/unknown        | 200              |
        |https://reqres.in/api/users?page=2 | 200             |



    Scenario Outline: GET request negative scenario
        Given the API endpoint <url>
        When I perform a GET request
        Then the response code for the GET request should be <status_code>

        Examples:
        |url                                                  | status_code|
        |https://reqres.in/api/unknown/23    | 404             |

    Scenario Outline: POST request
        Given the API endpoint <url>
        When I input a json '<path>' file
        And  I perform a POST request


        Examples:
        |url                                       | path           |
        |https://reqres.in/api/users    | ./json_data/user_data.json  |