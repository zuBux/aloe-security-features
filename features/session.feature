Feature: Session Management
		
		As a user
		I want my session to be securely managed
		So that a malicious user cannot impersonate me 

	Background:
	    Given a new browser instance

    Scenario: Session Fixation
        Given user testuser1 with password test1234 is logged in
        When user logs out
        And user testuser1 logs in with password test1234
        Then session tokens should be different

    Scenario: New session token issued after login
    	Given the homepage
    	And the value of the session token is saved
    	When user testuser1 logs in with password test1234 
    	Then session tokens should be different

    Scenario: Session token not accessible from JavaScript
    	When user testuser1 logs in with password test1234
    	Then session token should be flagged as HttpOnly

    Scenario: Session token should not be transmitted in plain HTTP
    	When user testuser1 logs in with password test1234
    	Then session token should be flagged as Secure
