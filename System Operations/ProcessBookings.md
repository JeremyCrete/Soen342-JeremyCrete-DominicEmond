## System Operation #1:
`SearchOffersAvailable();`

#### Operation Contract:
`SearchOffersAvailable`

#### Cross References:
Use Case - Process Bookings

#### Preconditions:
- The `Client` must be logged into the system.
- The `Client` must initiate a search request to view available offerings.

#### Postconditions:
- If available offers exist, the system retrieves and displays a list of offerings.
- If no offers are available, the system returns a `NoOffersAvailable` message.

## System Operation #2:
`BookOffering(Offer, Client);`

#### Operation Contract:
`BookOffering`

#### Cross References:
Use Case - Process Bookings

#### Preconditions:
- The `Offer` must exist and be available.
- The `Client` must be logged in and have selected an offer to book.
- The `Client` must be 18 years or older or have a guardian assigned.

#### Postconditions:
- A `Booking` object is created and linked to the `Client` and the `Offer`.
- The `Booking` is stored in the system.
- A confirmation message is returned to the `Client`.

## System Operation #3:
`Guardian();`

#### Operation Contract:
`Guardian`

#### Cross References:
Use Case - Process Bookings

#### Preconditions:
- The `Client` must be under 18 years of age.
- A `Guardian` must be registered and associated with the `Client`.

#### Postconditions:
- The `Guardian` is linked to the `Client` in the system.
- The `Guardian` details are validated and stored.
- The system allows the `Client` to proceed with bookings under the `Guardian`’s authorization.

## System Operation #4:
`GetMyBooking();`

#### Operation Contract:
`GetMyBooking`

#### Cross References:
Use Case - Process Bookings

#### Preconditions:
- The `Client` must be logged into the system.

#### Postconditions:
- The system retrieves all bookings associated with the `Client`.
- A list of bookings is displayed to the `Client`.

## System Operation #5:
`CancelTheBooking(booking);`

#### Operation Contract:
`CancelTheBooking`

#### Cross References:
Use Case - Process Bookings

#### Preconditions:
- The `Client` must have an existing `booking`.
- The `booking` must not have already been canceled.

#### Postconditions:
- The specified `booking` is marked as canceled in the system.
- The system sends a cancellation confirmation message to the `Client`.
- The canceled slot becomes available for other clients.

