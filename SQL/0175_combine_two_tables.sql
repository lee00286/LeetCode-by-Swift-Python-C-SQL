# Write your MySQL query statement below

#{"headers": {"Person": ["PersonId", "LastName", "FirstName"], "Address": ["AddressId", "PersonId", "City", "State"]}, "rows": {"Person": [[1, "Wang", "Allen"]], "Address": [[1, 2, "New York City", "New York"]]}}

# Person                               Address
# | PersonId | LastName | FirstName |  | AddressId | PersonId | City          | State    |
# +----------+----------+-----------+  +-----------+----------+---------------+----------+
# | 1        | Wang     | Allen     |  | 1         | 2        | New York City | New York |

SELECT firstName, lastName, city, state
FROM Person LEFT OUTER JOIN Address ON Person.personId = Address.personId;
