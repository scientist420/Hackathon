// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function () {

    // Search functionality
    const searchInput = document.getElementById('search');
    const filterButton = document.getElementById('filter');
    const hackathonList = document.getElementById('hackathon-list');

    // Mock data for hackathons (replace with API or database data)
    const hackathons = [
        {
            title: 'AI Innovation Challenge',
            description: 'Solve real-world AI problems',
            startDate: '2024-10-01',
            endDate: '2024-12-01'
        },
        {
            title: 'HealthTech Hackathon',
            description: 'Revolutionize healthcare with tech',
            startDate: '2024-11-05',
            endDate: '2024-11-15'
        }
        // Add more hackathons as needed
    ];

    // Function to display hackathons
    function displayHackathons(list) {
        hackathonList.innerHTML = ''; // Clear previous results
        list.forEach(hackathon => {
            const hackathonCard = `
                <div class="hackathon-card">
                    <h3>${hackathon.title}</h3>
                    <p>${hackathon.description}</p>
                    <p><strong>Start:</strong> ${hackathon.startDate} | <strong>End:</strong> ${hackathon.endDate}</p>
                </div>
            `;
            hackathonList.innerHTML += hackathonCard;
        });
    }

    // Initial display of all hackathons
    displayHackathons(hackathons);

    // Search function
    filterButton.addEventListener('click', function () {
        const query = searchInput.value.toLowerCase();
        const filteredHackathons = hackathons.filter(hackathon => 
            hackathon.title.toLowerCase().includes(query) ||
            hackathon.description.toLowerCase().includes(query)
        );
        displayHackathons(filteredHackathons);
    });
});
