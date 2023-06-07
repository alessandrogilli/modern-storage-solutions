# 01 - MongoDB
## Environment configuration
- Install [Docker and Docker compose](https://docs.docker.com/engine/install/)
- Inside this directory, open a terminal and run:
    
    ```docker compose up -d```

## MongoDB shell
Enter the shell:
```bash
docker exec -it mongo mongosh -u "root" -p "example"
```
Check the current database:
```
db
```
Insert a bunch of documents:
```json
db.movies.insertMany([
   {
      title: 'Titanic',
      year: 1997,
      genres: [ 'Drama', 'Romance' ],
      rated: 'PG-13',
      languages: [ 'English', 'French', 'German', 'Swedish', 'Italian', 'Russian' ],
      released: ISODate("1997-12-19T00:00:00.000Z"),
      awards: {
         wins: 127,
         nominations: 63,
         text: 'Won 11 Oscars. Another 116 wins & 63 nominations.'
      },
      cast: [ 'Leonardo DiCaprio', 'Kate Winslet', 'Billy Zane', 'Kathy Bates' ],
      directors: [ 'James Cameron' ]
   },
   {
      title: 'The Dark Knight',
      year: 2008,
      genres: [ 'Action', 'Crime', 'Drama' ],
      rated: 'PG-13',
      languages: [ 'English', 'Mandarin' ],
      released: ISODate("2008-07-18T00:00:00.000Z"),
      awards: {
         wins: 144,
         nominations: 106,
         text: 'Won 2 Oscars. Another 142 wins & 106 nominations.'
      },
      cast: [ 'Christian Bale', 'Heath Ledger', 'Aaron Eckhart', 'Michael Caine' ],
      directors: [ 'Christopher Nolan' ]
   },
   {
      title: 'Spirited Away',
      year: 2001,
      genres: [ 'Animation', 'Adventure', 'Family' ],
      rated: 'PG',
      languages: [ 'Japanese' ],
      released: ISODate("2003-03-28T00:00:00.000Z"),
      awards: {
         wins: 52,
         nominations: 22,
         text: 'Won 1 Oscar. Another 51 wins & 22 nominations.'
      },
      cast: [ 'Rumi Hiiragi', 'Miyu Irino', 'Mari Natsuki', 'Takashi Naitè' ],
      directors: [ 'Hayao Miyazaki' ]
   },
   {
      title: 'Casablanca',
      genres: [ 'Drama', 'Romance', 'War' ],
      rated: 'PG',
      cast: [ 'Humphrey Bogart', 'Ingrid Bergman', 'Paul Henreid', 'Claude Rains' ],
      languages: [ 'English', 'French', 'German', 'Italian' ],
      released: ISODate("1943-01-23T00:00:00.000Z"),
      directors: [ 'Michael Curtiz' ],
      awards: {
         wins: 9,
         nominations: 6,
         text: 'Won 3 Oscars. Another 6 wins & 6 nominations.'
      },
      lastupdated: '2015-09-04 00:22:54.600000000',
      year: 1942
   }
])
```
Query all documents:
```
db.movies.find( { } );
```

Query filtering data:
- Filter for director:
    ```
    db.movies.find( { "directors": "Christopher Nolan" } );
    ```
- Filter for language:
    ```
    db.movies.find( { "languages": { $in: [ "Japanese", "Mandarin" ] } } )
    ```
- Filter documents before a certain date:
    ```
    db.movies.find( { "released": { $lt: ISODate("2000-01-01") } } );
    ```
- Filter with a numerical range:
    ```
    db.movies.find( { "awards.wins": { $gt: 100 } } );
    ```
- Projections, to specify fields to return
    ```
    db.movies.find( { }, { "title": 1, "directors": 1, "year": 1 } );
    ```
    default value for fields to not project is zero:
    ```
    db.movies.find( { }, { "title": 0, "directors": 0, "year": 0 } );
    ```
- Aggregations:
    ```
    db.movies.aggregate( [
   { $unwind: "$genres" },
   {
     $group: {
       _id: "$genres",
       genreCount: { $count: { } }
     }
   },
   { $sort: { "genreCount": -1 } }
    ] )
    ```
## Connect to mongodb-express
http://localhost:8081



## Credits
https://www.mongodb.com/