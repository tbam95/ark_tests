class SqlQuery:
    def __init__(self):

        self.id     = ""
        self.url    = ""
        self.date   = ""
        self.rating = ""

    def generate(self, table):

        dict1 = {
          "id"    : self.id,
          "url"   : self.url,
          "date"  : self.date,
          "rating": self.rating
        }

        sql = list()
        sql.append("SELECT * FROM %s " % table)

        if dict1:
            sql.append("WHERE " + " AND ".join("%s" % (v) for k, v in dict1.items()))
        sql.append(";")

        return "".join(sql)

####################################
# Generate query example
####################################

query = SqlQuery()

#Set arguments
query.id     = "id IN list"
query.url    = "url = https://www.google.co.uk"
query.date   = "date > 2016-01-01"
query.rating = "2 < rating < 9"

print(query.generate("example_table"))