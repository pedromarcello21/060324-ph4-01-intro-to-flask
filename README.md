# Intro to Flask

## Learning Goals

- Request / Response cycle

- Model View Controller architecture

- Serving static information with GET routes

- `make_response` and `jsonify`

- Route parameters

## Request / Response Cycle

<img src="assets/request-response.png" alt="mvc architecture" width="80%" />

## Model View Controller Architecture

<img src="assets/mvc.png" alt="mvc architecture" width="80%" />

## Exercises

1. Create a route `GET /greeting`. This route responds with this json:

```
{ "response": "Hello!" }
```


2. Create a route `GET /count-to/:x`. It will respond with an array of numbers from `1` to `x` as JSON. For example `/count-to/5` would respond with:

```
[1,2,3,4,5]
```

3. Create a route `GET /lower-case/:word`. It will respond with the `word` parameter made lowercase. For example `/lower-case/HeLlO` would respond with:

```
{ "result": "hello" }
```