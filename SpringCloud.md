# Spring Cloud

## Spring Cloud Gateway

1. zuul 1
	- 비동기를 지원하지 않아, websocket을 사용하는데 무리가 있을것으로 생각됨.
	- 우회해서 해결할 수 있을 것으로 생각되나, 굳이 옛 기술을 사용할 필요는 없을 것으로 생각됨
2. zuul 2.0
	- netty 서버가 request를 받아, inboud filter, endpoint filter, outbound filter를 거쳐 response하는 구조를 채용
	- 비동기를 지원
	- 하위 호환성 없음
	- Spring Eco System의 취지와 맞지 않아, Spring Cloud Gateway를 새로 제작
3. Spring Cloud Gateway 

![](https://cloud.spring.io/spring-cloud-gateway/reference/html/images/spring_cloud_gateway_diagram.png) 

Spring Cloud Gateway 기본 구조


```
@Bean public RouteLocator myRoutes(RouteLocatorBuilder builder) { 
    return builder.routes()  
            .route(p -> p  
                    .path("/**")  
                    .filters(f -> f.rewritePath("^\\/[0-9a-zA-Z\\/]*$", "/login"))  
                    .uri("lb://AUTH-SERVICE")  
                    .predicate(pre -> pre.getRequest().getCookies().isEmpty()))  
            .route(p -> p  
                    .path("/auth")  
                    .uri("lb://AUTH-SERVICE"))  
            .build();
}
```

다음과 같은 포멧으로 작성 path + predicate 로 적절한 라우팅을 찾고, filter를 거쳐 uri로 라우팅한다.


Jackson은 get메소드를 호출해서 작동함


.filters(f -> f.setResponseHeader("X-Frame-Options", "ALLOW-FROM http://localhost:9001/"))
크롬에서 지원하지 않는것을 확인

STOMP connect를 생성할 때 8080으로 생성할 경우, iframe들이 8080에 묶이는 모양이다. 하지만 실질적으로 통신하는 서버는 9000이기 떄문에 Cross Origin Frame 에러가 발생한 것,,,

따라서 connection을 생성할 때 9000으로 직접 생성하니깐 되더라...