# QueueJobs using subscription ( client Python )

Prisma with DB working on Docker<br>
Python consume GraphQL API <b>( at this moment only working Query)</b>

<a href="http://pl.tinypic.com?ref=wslgsn" target="_blank"><img src="http://i64.tinypic.com/wslgsn.jpg" border="0" alt="Image and video hosting by TinyPic"></a>

## Instalation

```
0. cd JobQueueService/
1. cd prisma
2. docker-compose up -d ( need docker deamon )
3. cd ..
4. yarn or npm install
5. prisma deploy ( prisma 1.14 need )
6. prisma seed
7. prisma playground
```

## Where is model data

```
JobQueueService > Prisma > datamodel.graphql
```

## Sample subscription - view all operation on model QueueJob

```
subscription {
  queueJobs{
    node{
      id
      status
      params
      dataIn
      jobInfo {
        jobType
        jobGroup
      }
      createdAt
    }
  }
}
```

## Sample mutation

in file seed.graphql you will see some examples
