Feature: Sample API Test


Scenario: Validate API GET request
    Given I have a REST API endpoint "https://jsonplaceholder.typicode.com/posts/1"
    When I send a GET request to the endpoint
    Then I should get a 200 response code
    And the response should contain the key "userId"