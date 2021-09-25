using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ResManager
{
	private static ResManager instance;
	private ResManager()
	{

	}
	public static ResManager Instance
	{
		get
		{
			if (instance == null)
			{
				instance = new ResManager();
				instance.Init();
			}
			return instance;
		}
	}
	private void Init()
	{
		
	}
}