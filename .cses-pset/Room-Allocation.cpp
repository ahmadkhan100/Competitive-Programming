#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

struct Customer {
    int arrival;
    int departure;
    int index;
};

int main() {
    // Fast I/O optimization
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<Customer> customers(n);
    for (int i = 0; i < n; ++i) {
        cin >> customers[i].arrival >> customers[i].departure;
        customers[i].index = i;
    }

    // Sort customers by arrival day
    sort(customers.begin(), customers.end(), [](const Customer& a, const Customer& b) {
        return a.arrival < b.arrival;
    });

    // Min-heap to keep track of occupied rooms (departure_day, room_number)
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> occupied_rooms;
    // Min-heap to keep track of available room numbers
    priority_queue<int, vector<int>, greater<int>> available_rooms;

    vector<int> room_assignments(n);
    int total_rooms = 0;

    for (const auto& customer : customers) {
        int arrival = customer.arrival;
        int departure = customer.departure;
        int idx = customer.index;

        // Free up rooms that have become available
        while (!occupied_rooms.empty() && occupied_rooms.top().first < arrival) {
            int freed_room_number = occupied_rooms.top().second;
            occupied_rooms.pop();
            available_rooms.push(freed_room_number);
        }

        int room_number;
        if (!available_rooms.empty()) {
            // Reuse an available room
            room_number = available_rooms.top();
            available_rooms.pop();
        } else {
            // Assign a new room
            total_rooms++;
            room_number = total_rooms;
        }

        // Assign the room to the current customer
        room_assignments[idx] = room_number;
        // Mark the room as occupied until the customer's departure
        occupied_rooms.emplace(departure, room_number);
    }

    // Output the results
    cout << total_rooms << '\n';
    for (int i = 0; i < n; ++i) {
        cout << room_assignments[i] << (i < n - 1 ? ' ' : '\n');
    }

    return 0;
}
