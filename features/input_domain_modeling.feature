Feature: Input Domain Modeling

  Scenario: Generate combinations using ACoc mode
    Given the characteristics "size:S,M,L" and "color:Red,Green,Blue"
    And the abstract blocks "shirt:size,color"
    When I run the script with mode "ACoc"
    Then the output should be:
      """
      ('S', 'Red')
      ('S', 'Green')
      ('S', 'Blue')
      ('M', 'Red')
      ('M', 'Green')
      ('M', 'Blue')
      ('L', 'Red')
      ('L', 'Green')
      ('L', 'Blue')
      """

  Scenario: Generate combinations using MBCC mode
    Given the characteristics "size:S,M,L" and "color:Red,Green,Blue"
    And the abstract blocks "shirt:size,color"
    When I run the script with mode "MBCC"
    Then the output should be:
      """
      ['S', 'Red']
      """

  Scenario: Generate combinations using ECC mode
    Given the characteristics "size:S,M,L" and "color:Red,Green,Blue"
    And the abstract blocks "shirt:size,color"
    When I run the script with mode "ECC"
    Then the output should be:
      """
      ['S']
      ['M']
      ['L']
      ['Red']
      ['Green']
      ['Blue']
      """

  Scenario: Generate combinations using BCC mode
    Given the characteristics "size:S,M,L" and "color:Red,Green,Blue"
    And the abstract blocks "shirt:size,color"
    When I run the script with mode "BCC"
    Then the output should be:
      """
      ['S', 'Red']
      """
