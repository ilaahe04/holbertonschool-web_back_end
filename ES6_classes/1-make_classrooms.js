// Import the ClassRoom class from the specified file
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
    return [
        new ClassRoom(19),
        new ClassRoom(20),
        new ClassRoom(34)
    ];
}
