using UnityEngine;
using System.Net.Sockets;
using System.Text;

public class MySender : MonoBehaviour
{
    public string serverHost = "127.0.0.1";
    public int serverPort = 25001;

    void Start()
    {
        // Create a TCP client
        TcpClient client = new TcpClient();

        try
        {
            // Connect to the server
            client.Connect(serverHost, serverPort);

            // Get the Scale of the object
            Vector3 Scale = transform.localScale;

            // Convert the Scale to a string
            string dataToSend = Scale.x + "," + Scale.y + "," + Scale.z;

            // Send the data
            NetworkStream stream = client.GetStream();
            byte[] data = Encoding.UTF8.GetBytes(dataToSend);
            stream.Write(data, 0, data.Length);
            Debug.Log("Sent data to Python: " + dataToSend);
        }
        catch (System.Exception e)
        {
            Debug.LogError("Error sending data to Python: " + e.Message);
        }
        finally
        {
            // Close the client
            client.Close();
        }
    }
}
