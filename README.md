# QueueJobs

Prisma with DB working on Docker
Python consume GraphQL API ( at this moment only working Query)

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
