# :dollar: account-book
페이히어 가계부 서비스 개발

# :bookmark_tabs: 목차
* [account-book](#account-book)
  * [목차](#목차)
  * [프로젝트 요구사항](#프로젝트-요구사항)
  * [API Docs](#api-docs)
    * [회원 가입](#회원-가입)
    * [로그인](#로그인)
    * [로그아웃](#로그아웃)
    * [가계부 등록](#가계부-등록)
    * [가계부 목록](#가계부-목록)
    * [가계부 상세](#가계부-상세)
    * [가계부 수정](#가계부-수정)
    * [가계부 삭제](#가계부-삭제)
    * [가계부 삭제 목록](#가계부-삭제-목록)
    * [가계부 삭제 복구](#가계부-삭제-복구)


# :clipboard: 프로젝트 요구사항
1. 고객은 이메일과 비밀번호 입력을 통해서 회원가입을 할 수 있습니다.
2. 고객은 회원 가입이후, 로그인과 로그아웃을 할 수 있습니다.
3. 고객은 로그인 이후 가계부 관련 아래의 행동을 할 수 있습니다.
   * 가계부에 오늘 사용한 돈의 금액과 관련된 메모를 남길 수 있습니다.
   * 가계부에서 수정을 원하는 내역은 금액과 메모를 수정할 수 있습니다.
   * 가계부에서 삭제를 원하는 내역은 삭제를 할 수 있습니다.
   * 삭제한 내역은 언제든지 다시 복수 할 수 있습니다.
   * 가계부에서 이제까지 기록한 가계부 리스트를 볼 수 있습니다.
   * 가계부에서 상세한 세부 내역을 볼 수 있습니다.
4. 로그인하지 않은 고객은 가계부 내역에 대한 접근 제한 처리가 되어야 합니다.

# :books: API Docs
## 회원 가입

> Method: POST<br>
URL: /api/v1/users/register/<br>
Description: SimpleJWT Token 발행<br>
Request Example
```json
{
    "username": "test@test.com",
    "password": "12341234"
}
```
> Response Example
```json
{
    "username": "test2@test.com"
}
```
##  로그인
> Method: POST<br>
URL: /api/v1/users/login/<br>
Request Example
```json
{
    "username": "test@test.com",
    "password": "12341234"
}
```
> Response Example
```json
{
    "refresh": "token_key1",
    "access": "token_key2"
}
```
##  로그아웃(* TODO *)
> Method: POST<br>
URL: /api/v1/users/logout/<br>
Request Example
```json
{
    TODO
}
```
> Response Example
```json
{
    TODO
}
```
##  가계부 등록
> Method: POST<br>
URL: /api/v1/accounts/<br>
Request Example
```json
{
    "amount": 5000,
    "memo": "맥주 한 잔"
}
```
> Response Example
```json
{
    "amount": 5000,
    "memo": "맥주 한 잔",
    "is_delete": false
}
```
##  가계부 목록
> Method: GET<br>
URL: /api/v1/accounts/<br>
Responses
```json
[
    {
        "amount": 5000,
        "memo": "맥주 한 잔",
        "is_delete": false
    },
    {
        "amount": 15000,
        "memo": "맥주 세 잔",
        "is_delete": false
    },
    ...
]
```
##  가계부 상세
> Method: GET<br>
URL: /api/v1/accounts/account_id/<br>
Responses
```json
{
    "amount": 5000,
    "memo": "맥주 한 잔",
    "is_delete": false
}
```
##  가계부 수정
> Method: PUT<br>
URL: /api/v1/accounts/account_id/<br>
Request Example
```json
{
    "amount": 15000,
    "memo": "맥주 세 잔",
    "is_delete": false
}
```
> Response Example
```json
{
    "amount": 15000,
    "memo": "맥주 세 잔",
    "is_delete": false
}
```
##  가계부 삭제
> Method: DELETE<br>
URL: /api/v1/accounts/account_id/<br>
##  가계부 삭제 목록
> Method: GET<br>
URL: /api/v1/accounts/restoration/<br>
Resonse
```json
[
    {
        "amount": 5000,
        "memo": "맥주 한 잔",
        "is_delete": true
    },
    {
        "amount": 15000,
        "memo": "맥주 세 잔",
        "is_delete": true
    },
    ...
]
```
##  가계부 삭제 복구
> Method: POST<br>
URL: /api/v1/accounts/restoration/account_id/<br>
Resonse Example
```json
{
    "amount": 15000,
    "memo": "맥주 세 잔",
    "is_delete": false
}
```

