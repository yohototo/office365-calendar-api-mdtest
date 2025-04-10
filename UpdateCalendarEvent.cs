using Microsoft.Graph;
using Microsoft.Identity.Client;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Office365Calendar
{
    class UpdateCalendarEvent
    {
        // The client ID of your registered application
        private static string clientId = "YOUR_CLIENT_ID";

        // The authority of your identity provider
        private static string authority = "https://login.microsoftonline.com/YOUR_TENANT_ID";

        // The scopes required to access the calendar
        private static string[] scopes = new string[] { "Calendars.ReadWrite" };

        // The ID of the event to update
        private static string eventId = "YOUR_EVENT_ID";

        // The GraphServiceClient instance
        private static GraphServiceClient graphClient;

        static async Task Main(string[] args)
        {
            try
            {
                // Initialize the authentication provider
                var authProvider = new InteractiveAuthenticationProvider(
                    PublicClientApplicationBuilder.Create(clientId)
                    .WithAuthority(authority)
                    .Build(),
                    scopes);

                // Initialize the GraphServiceClient
                graphClient = new GraphServiceClient(authProvider);

                // Update the event
                await UpdateEventAsync();

                Console.WriteLine("Event updated successfully.");

                // Verify the updated event
                await VerifyUpdatedEventAsync();
            }
            catch (ServiceException ex)
            {
                Console.WriteLine($"Graph API error: {ex.Message}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"General error: {ex.Message}");
            }
        }

        private static async Task UpdateEventAsync()
        {
            try
            {
                // Get the event to update
                var eventToUpdate = await graphClient.Me.Events[eventId].Request().GetAsync();

                // Modify the event properties
                eventToUpdate.Subject = "New subject"; // Change the event subject
                eventToUpdate.Start.DateTime = "2024-03-01T10:00:00"; // Change the event start time
                eventToUpdate.End.DateTime = "2024-03-01T11:00:00"; // Change the event end time
                eventToUpdate.Location = new Location { DisplayName = "New location" }; // Change the event location
                eventToUpdate.Attendees = new List<Attendee> // Change the event attendees
                {
                    new Attendee
                    {
                        EmailAddress = new EmailAddress
                        {
                            Address = "user1@example.com",
                            Name = "User One"
                        },
                        Type = AttendeeType.Required
                    },
                    new Attendee
                    {
                        EmailAddress = new EmailAddress
                        {
                            Address = "user2@example.com",
                            Name = "User Two"
                        },
                        Type = AttendeeType.Optional
                    }
                };

                // Update the event
                await graphClient.Me.Events[eventId].Request().UpdateAsync(eventToUpdate);
            }
            catch (ServiceException ex)
            {
                Console.WriteLine($"Error updating event: {ex.Message}");
                throw;
            }
        }

        private static async Task VerifyUpdatedEventAsync()
        {
            try
            {
                // Retrieve the updated event
                var updatedEvent = await graphClient.Me.Events[eventId].Request().GetAsync();

                // Log updated event details
                Console.WriteLine("\nUpdated Event Details:");
                Console.WriteLine($"Subject: {updatedEvent.Subject}");
                Console.WriteLine($"Start: {updatedEvent.Start.DateTime}");
                Console.WriteLine($"End: {updatedEvent.End.DateTime}");
                Console.WriteLine($"Location: {updatedEvent.Location?.DisplayName}");

                Console.WriteLine("Attendees:");
                foreach (var attendee in updatedEvent.Attendees)
                {
                    Console.WriteLine($"- {attendee.EmailAddress.Name} ({attendee.EmailAddress.Address}), Type: {attendee.Type}");
                }
            }
            catch (ServiceException ex)
            {
                Console.WriteLine($"Error verifying updated event: {ex.Message}");
            }
        }
    }
}
# coms nin weishenme buxing jingxingaweibimg
